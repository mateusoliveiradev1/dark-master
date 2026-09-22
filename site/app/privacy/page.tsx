import type { Metadata } from "next";
import { Nav } from "@/components/Nav";
import { Logo } from "@/components/Logo";

export const metadata: Metadata = {
  title: "Política de Privacidade — dark-master",
  description: "Como o dark-master acessa, usa e protege os dados do YouTube.",
};

export default function Privacy() {
  return (
    <>
      <Nav />
      <main className="doc">
        <p className="eyebrow" style={{ marginTop: 48 }}>Documento legal</p>
        <h1>Política de Privacidade</h1>
        <p className="muted">Última atualização: 21 de setembro de 2026.</p>

        <p>Esta política descreve como o projeto <strong>dark-master</strong> (&quot;nós&quot;, &quot;a skill&quot;) acessa, usa e protege dados ao se conectar à API do YouTube em nome do usuário.</p>

        <div className="note">
          O uso, por parte do dark-master, de informações recebidas das APIs do Google obedece à{" "}
          <a href="https://developers.google.com/terms/api-services-user-data-policy" target="_blank" rel="noopener">Google API Services User Data Policy</a>,
          incluindo os requisitos de <strong>Uso Limitado (Limited Use)</strong>.
        </div>

        <h2>1. Quais dados acessamos</h2>
        <p>Com a sua autorização explícita via login do Google (OAuth 2.0), a skill pode ler, <strong>somente do canal que você autorizar</strong>:</p>
        <ul>
          <li>Métricas do YouTube Analytics (views, tempo de exibição, retenção, inscritos, receita estimada);</li>
          <li>Metadados públicos dos vídeos e da conta (títulos, datas, identificadores).</li>
        </ul>
        <p>Todos os escopos são de <strong>leitura</strong>: <code>youtube.readonly</code>, <code>yt-analytics.readonly</code> e <code>yt-analytics-monetary.readonly</code>. Não publicamos, editamos ou apagamos nada no seu canal.</p>

        <h2>2. Como usamos os dados</h2>
        <p>Exclusivamente para análise e melhoria de desempenho do seu próprio canal — identificar vídeos de destaque (&quot;outliers&quot;), retenção, conversões e oportunidades de conteúdo. Sem publicidade, perfilamento de terceiros ou qualquer fim alheio a essa análise.</p>

        <h2>3. Onde os dados ficam armazenados</h2>
        <ul>
          <li>As credenciais (<code>client_secrets.json</code>, <code>yt-token.json</code>) e a string de banco (<code>dark.env</code>) ficam <strong>na sua máquina</strong>, fora do repositório.</li>
          <li>As métricas são gravadas no <strong>seu próprio banco</strong> (Postgres/Neon que você configurar) ou localmente (SQLite).</li>
        </ul>

        <h2>4. Compartilhamento</h2>
        <p><strong>Não vendemos, alugamos nem compartilhamos</strong> seus dados. Não há rastreamento, analytics de terceiros ou anúncios. Exceto por exigência legal, os dados não saem do seu controle.</p>

        <h2>5. Retenção e exclusão</h2>
        <ul>
          <li>Revogue o acesso a qualquer momento em <a href="https://myaccount.google.com/permissions" target="_blank" rel="noopener">myaccount.google.com/permissions</a>.</li>
          <li>Para apagar os dados locais, remova a pasta de segredos e o banco.</li>
          <li>Tokens em modo &quot;Teste&quot; do Google expiram automaticamente; reautorize quando quiser.</li>
        </ul>

        <h2>6. Segurança</h2>
        <p>Menor privilégio (apenas leitura) e credenciais fora de qualquer repositório versionado. Nenhum método é 100% infalível; mantenha suas chaves privadas.</p>

        <h2>7. Cookies e hospedagem</h2>
        <p>Site estático, sem cookies próprios. A hospedagem (Vercel) e as fontes (Google Fonts) podem registrar dados técnicos conforme suas próprias políticas.</p>

        <h2>8. Menores</h2>
        <p>Não destinada a menores de 13 anos; não coletamos dados de crianças intencionalmente.</p>

        <h2>9. Alterações</h2>
        <p>Podemos atualizar esta política. A data no topo indica a última revisão.</p>

        <h2>10. Contato</h2>
        <p>Dúvidas: <a href="mailto:warface01031999@gmail.com">warface01031999@gmail.com</a>.</p>
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
