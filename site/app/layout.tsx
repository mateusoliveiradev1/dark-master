import type { Metadata, Viewport } from "next";
import { Bebas_Neue, Space_Grotesk, JetBrains_Mono } from "next/font/google";
import "./globals.css";
import { Providers } from "@/lib/store";
import { Cursor } from "@/components/Cursor";
import { Background } from "@/components/Background";

const display = Bebas_Neue({ weight: "400", subsets: ["latin"], variable: "--font-display", display: "swap" });
const sans = Space_Grotesk({ subsets: ["latin"], variable: "--font-sans", display: "swap" });
const mono = JetBrains_Mono({ subsets: ["latin"], variable: "--font-mono", display: "swap" });

const googleVerify = process.env.NEXT_PUBLIC_GOOGLE_SITE_VERIFICATION;

export const metadata: Metadata = {
  title: "dark-master — a skill que faz canais dark virarem negócio",
  description:
    "Planeja, produz e monetiza canais dark/faceless no YouTube: algoritmo, roteiro, thumbnails, Shorts, outliers e auto-evolução com dados reais.",
  metadataBase: new URL("https://dark-master.vercel.app"),
  openGraph: {
    title: "dark-master",
    description: "Da ideia ao monetizado: a skill de canais dark no YouTube.",
    type: "website",
    url: "https://dark-master.vercel.app",
  },
  ...(googleVerify ? { verification: { google: googleVerify } } : {}),
};

export const viewport: Viewport = { themeColor: "#070709" };

const themeScript = `(function(){try{var t=localStorage.getItem('dm-theme')||'dark';document.documentElement.dataset.theme=t;var l=localStorage.getItem('dm-lang');if(l)document.documentElement.lang=l;}catch(e){document.documentElement.dataset.theme='dark';}})();`;

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="pt-BR" data-theme="dark" className={`${display.variable} ${sans.variable} ${mono.variable}`}>
      <head>
        <script dangerouslySetInnerHTML={{ __html: themeScript }} />
      </head>
      <body>
        <Providers>
          <Background />
          <Cursor />
          {children}
        </Providers>
      </body>
    </html>
  );
}
