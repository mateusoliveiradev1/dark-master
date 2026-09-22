"use client";
import { createContext, useContext, useEffect, useState, type ReactNode } from "react";
import { dict, type Dict, type Lang } from "./dict";

type Theme = "dark" | "light";

type Ctx = { lang: Lang; setLang: (l: Lang) => void; t: Dict; theme: Theme; toggleTheme: () => void };

const I18n = createContext<Ctx | null>(null);

export function Providers({ children }: { children: ReactNode }) {
  const [lang, setLangState] = useState<Lang>("pt");
  const [theme, setTheme] = useState<Theme>("dark");

  useEffect(() => {
    const savedLang = (localStorage.getItem("dm-lang") as Lang) || "pt";
    const savedTheme = (localStorage.getItem("dm-theme") as Theme) || "dark";
    setLangState(savedLang);
    setTheme(savedTheme);
    document.documentElement.lang = savedLang;
    document.documentElement.dataset.theme = savedTheme;
  }, []);

  const setLang = (l: Lang) => {
    setLangState(l);
    localStorage.setItem("dm-lang", l);
    document.documentElement.lang = l;
  };
  const toggleTheme = () => {
    setTheme((prev) => {
      const next = prev === "dark" ? "light" : "dark";
      localStorage.setItem("dm-theme", next);
      document.documentElement.dataset.theme = next;
      return next;
    });
  };

  return <I18n.Provider value={{ lang, setLang, t: dict[lang], theme, toggleTheme }}>{children}</I18n.Provider>;
}

export function useI18n() {
  const ctx = useContext(I18n);
  if (!ctx) throw new Error("useI18n must be used within Providers");
  return ctx;
}
