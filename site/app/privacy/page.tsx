import type { Metadata } from "next";
import { PrivacyContent } from "@/components/PrivacyContent";

export const metadata: Metadata = {
  title: "Política de Privacidade — dark-master",
  description: "Como o dark-master acessa, usa e protege os dados do YouTube.",
};

export default function Privacy() {
  return <PrivacyContent />;
}
