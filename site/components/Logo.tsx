"use client";
import { motion } from "framer-motion";

export function Logo({ size = 28 }: { size?: number }) {
  return (
    <svg width={size} height={size} viewBox="0 0 64 64" fill="none" aria-hidden="true">
      <defs>
        <linearGradient id="lg" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0" stopColor="#e23b3b" />
          <stop offset="1" stopColor="#B91C1C" />
        </linearGradient>
      </defs>
      <motion.path
        d="M8 18 L8 52 L56 52 L56 18 L32 18 L27 12 L8 12 Z"
        fill="#111114"
        stroke="#F5F5F4"
        strokeWidth={2.2}
        strokeLinejoin="round"
        initial={{ pathLength: 0, opacity: 0 }}
        animate={{ pathLength: 1, opacity: 1 }}
        transition={{ duration: 1.1, ease: "easeInOut" }}
      />
      <motion.path d="M8 26 L56 26" stroke="#26262c" strokeWidth={2.2}
        initial={{ pathLength: 0 }} animate={{ pathLength: 1 }} transition={{ duration: 0.6, delay: 0.5 }} />
      <motion.g initial={{ opacity: 0, scale: 0.6 }} animate={{ opacity: 1, scale: 1 }}
        transition={{ delay: 0.7, type: "spring", stiffness: 200, damping: 14 }} style={{ originX: "38px", originY: "36px" }}>
        <circle cx="38" cy="36" r="8" stroke="url(#lg)" strokeWidth={2.6} />
        <path d="M44 42 L50 48" stroke="url(#lg)" strokeWidth={3.2} strokeLinecap="round" />
      </motion.g>
      <motion.rect x="14" y="31" width="12" height="3.4" rx="1.2" fill="#e23b3b"
        initial={{ opacity: 0, scaleX: 0 }} animate={{ opacity: 1, scaleX: 1 }}
        transition={{ delay: 1, type: "spring", stiffness: 300, damping: 18 }} style={{ originX: "14px" }} />
    </svg>
  );
}
