import { NextResponse } from "next/server";
import { createHash, timingSafeEqual } from "node:crypto";

function expected(): string | null {
  const secret = process.env.PAINEL_SENHA;
  if (!secret) return null;
  return createHash("sha256").update(`dm:${secret}`).digest("hex");
}

export async function POST(request: Request) {
  const want = expected();
  if (!want) return NextResponse.json({ ok: false }, { status: 503 });
  const { senha } = (await request.json().catch(() => ({}))) as { senha?: string };
  if (typeof senha !== "string" || !senha) return NextResponse.json({ ok: false }, { status: 401 });
  const got = createHash("sha256").update(`dm:${senha}`).digest();
  const wantBuf = Buffer.from(want, "hex");
  if (got.length !== wantBuf.length || !timingSafeEqual(got, wantBuf)) {
    return NextResponse.json({ ok: false }, { status: 401 });
  }
  const response = NextResponse.json({ ok: true });
  response.cookies.set("dm_auth", want, { httpOnly: true, sameSite: "lax", path: "/", maxAge: 60 * 60 * 24 * 30 });
  return response;
}

export async function DELETE() {
  const response = NextResponse.json({ ok: true });
  response.cookies.delete("dm_auth");
  return response;
}
