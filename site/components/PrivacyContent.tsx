"use client";
import { Nav } from "@/components/Nav";
import { Logo } from "@/components/Logo";
import { useI18n } from "@/lib/store";

export function PrivacyContent() {
  const { t } = useI18n();
  return (
    <>
      <Nav />
      <main className="doc">
        <p className="eyebrow" style={{ marginTop: 48 }}>Documento legal</p>
        <h1>{t.privacy.title}</h1>
        <p className="muted">{t.privacy.updated}</p>
        <p>{t.privacy.intro}</p>
        <div className="note">
          O uso, por parte do dark-master, de informações recebidas das APIs do Google obedece à{" "}
          <a href="https://developers.google.com/terms/api-services-user-data-policy" target="_blank" rel="noopener">
            Google API Services User Data Policy
          </a>
          , incluindo os requisitos de <strong>Uso Limitado (Limited Use)</strong>.
        </div>
        {t.privacy.sections.map(([title, body]) => (
          <section key={title} style={{ borderBottom: "none", padding: 0 }}>
            <h2>{title}</h2>
            <p>{body}</p>
          </section>
        ))}
      </main>
      <footer style={{ borderTop: "1px solid var(--line)", marginTop: 56 }}>
        <div className="wrap foot">
          <a className="brand" href="/"><Logo /> dark-master</a>
          <p className="muted">Documento que atende aos requisitos de exibição da Tela de permissão OAuth do Google.</p>
        </div>
      </footer>
    </>
  );
}
