export default function robots() {
  return {
    rules: [{ userAgent: "*", allow: ["/"], disallow: ["/dashboard", "/dashboard.json", "/api/", "/login"] }],
    sitemap: "https://dark-master.vercel.app/sitemap.xml",
  };
}
