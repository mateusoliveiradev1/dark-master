"use client";
import { useState } from "react";
import { motion } from "framer-motion";
import { useI18n } from "@/lib/store";
import { Reveal } from "./Reveal";

const VIDEO_ID = "FiWWSWJoOW8"; // Springfield Three — best-performing Short (loop)

export function VideoSection() {
  const { t } = useI18n();
  const [play, setPlay] = useState(false);

  return (
    <section id="video" style={{ borderBottom: "none" }}>
      <div className="wrap">
        <Reveal>
          <div className="sec-head">
            <div>
              <p className="eyebrow">{t.video.eyebrow}</p>
              <h2>{t.video.title}</h2>
            </div>
            <p>{t.video.sub}</p>
          </div>
        </Reveal>

        <Reveal delay={0.08}>
          <div className="video-shell">
            {play ? (
              <iframe
                src={`https://www.youtube.com/embed/${VIDEO_ID}?autoplay=1&rel=0&modestbranding=1`}
                title="Cold File Diaries — sample"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowFullScreen
              />
            ) : (
              <button className="video-facade" onClick={() => setPlay(true)} aria-label="Play">
                <img src={`https://i.ytimg.com/vi/${VIDEO_ID}/maxresdefault.jpg`} alt="" loading="lazy" />
                <span className="video-veil" />
                <motion.span
                  className="play"
                  initial={{ scale: 0.9, opacity: 0 }}
                  whileInView={{ scale: 1, opacity: 1 }}
                  viewport={{ once: true }}
                  transition={{ type: "spring", stiffness: 200, damping: 14 }}
                >
                  <svg width="26" height="26" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z" /></svg>
                </motion.span>
                <span className="video-meta">
                  <b>COLD FILE DIARIES</b> · Springfield Three · 9:16
                </span>
              </button>
            )}
          </div>
          <div className="video-foot">
            <a className="btn" href={`https://www.youtube.com/watch?v=${VIDEO_ID}`} target="_blank" rel="noopener">
              <span />{t.video.watch}
            </a>
          </div>
        </Reveal>
      </div>
    </section>
  );
}
