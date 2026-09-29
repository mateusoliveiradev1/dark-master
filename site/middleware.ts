import { NextResponse, type NextRequest } from "next/server";

const COOKIE = "dm_auth";

async function expectedHash(): Promise<string | null> {
  const secret = process.env.PAINEL_SENHA;
  if (!secret) return null;
  const digest = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(`dm:${secret}`));
  return [...new Uint8Array(digest)].map((b) => b.toString(16).padStart(2, "0")).join("");
}

export async function middleware(request: NextRequest) {
  const expected = await expectedHash();
  if (!expected) {
    if (process.env.VERCEL) {
      return new NextResponse("Painel desabilitado: configure PAINEL_SENHA.", { status: 503 });
    }
    return NextResponse.next();
  }
  if (request.cookies.get(COOKIE)?.value === expected) return NextResponse.next();
  const login = new URL("/login", request.url);
  login.searchParams.set("next", request.nextUrl.pathname);
  return NextResponse.redirect(login);
}

export const config = {
  matcher: ["/dashboard", "/dashboard/:path*", "/dashboard.json"],
};
