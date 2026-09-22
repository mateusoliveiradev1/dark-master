import type { Metadata, Viewport } from "next";
import { Bebas_Neue, Space_Grotesk, JetBrains_Mono } from "next/font/google";
import "./globals.css";
import { Cursor } from "@/components/Cursor";
import { Background } from "@/components/Background";

const display = Bebas_Neue({ weight: "400", subsets: ["latin"], variable: "--font-display", display: "swap" });
const sans = Space_Grotesk({ subsets: ["latin"], variable: "--font-sans", display: "swap" });
const mono = JetBrains_Mono({ subsets: ["latin"], variable: "--font-mono", display: "swap" });

export const metadata: Metadata = {
  title: "dark-master — a skill que faz canais dark virarem negócio",
  description:
    "Planeja, produz e monetiza canais dark/faceless no YouTube: algoritmo, roteiro, thumbnails, Shorts, outliers e auto-evolução com dados reais.",
  openGraph: {
    title: "dark-master",
    description: "Da ideia ao monetizado: a skill de canais dark no YouTube.",
    type: "website",
  },
};

export const viewport: Viewport = {
  themeColor: "#070709",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="pt-BR" className={`${display.variable} ${sans.variable} ${mono.variable}`}>
      <body>
        <Background />
        <Cursor />
        {children}
      </body>
    </html>
  );
}
