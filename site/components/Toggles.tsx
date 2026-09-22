"use client";
import { useI18n } from "@/lib/store";

export function Toggles() {
  const { lang, setLang, theme, toggleTheme } = useI18n();
  return (
    <div className="toggles">
      <button className="chip" onClick={() => setLang(lang === "pt" ? "en" : "pt")} aria-label="Idioma / Language">
        {lang.toUpperCase()}
      </button>
      <button className="chip icon" onClick={toggleTheme} aria-label="Tema / Theme">
        {theme === "dark" ? (
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><circle cx="12" cy="12" r="4" /><path d="M12 2v2M12 20v2M2 12h2M20 12h2M5 5l1.5 1.5M17.5 17.5L19 19M19 5l-1.5 1.5M6.5 17.5L5 19" /></svg>
        ) : (
          <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8Z" /></svg>
        )}
      </button>
    </div>
  );
}
