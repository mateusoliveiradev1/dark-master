"use client";
import { useState } from "react";
import { useRouter, useSearchParams } from "next/navigation";
import { Suspense } from "react";
import { useI18n } from "@/lib/store";

function Form() {
  const { lang } = useI18n();
  const router = useRouter();
  const next = useSearchParams().get("next") || "/dashboard";
  const [senha, setSenha] = useState("");
  const [erro, setErro] = useState(false);
  const [indo, setIndo] = useState(false);
  const pt = lang === "pt";

  const entrar = async (e: React.FormEvent) => {
    e.preventDefault();
    setIndo(true);
    setErro(false);
    const r = await fetch("/api/auth", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ senha }),
    });
    if (r.ok) router.push(next);
    else {
      setErro(true);
      setIndo(false);
    }
  };

  return (
    <main id="top">
      <div className="wrap" style={{ maxWidth: 480, paddingTop: 90, paddingBottom: 90 }}>
        <p className="tag"><i />{pt ? "acesso restrito" : "restricted"}</p>
        <h1 style={{ fontSize: "clamp(38px,7vw,72px)" }}>{pt ? "Painel pessoal." : "Personal panel."}</h1>
        <p className="lead">{pt ? "Digite a senha para ver os dados dos seus canais." : "Enter the password to see your channels' data."}</p>
        <form onSubmit={entrar} style={{ display: "flex", gap: 12, marginTop: 24 }}>
          <input
            type="password"
            value={senha}
            onChange={(e) => setSenha(e.target.value)}
            placeholder="••••••••"
            autoFocus
            style={{ flex: 1, background: "var(--panel)", border: "1px solid var(--line-2)", color: "var(--bone)", padding: "13px 16px", fontSize: 16 }}
          />
          <button className="btn primary" type="submit" disabled={indo || !senha}>
            <span />{indo ? "…" : pt ? "Entrar" : "Enter"}
          </button>
        </form>
        {erro && <p style={{ color: "var(--red-bright)", marginTop: 12 }}>{pt ? "Senha incorreta." : "Wrong password."}</p>}
      </div>
    </main>
  );
}

export default function LoginPage() {
  return (
    <Suspense>
      <Form />
    </Suspense>
  );
}
