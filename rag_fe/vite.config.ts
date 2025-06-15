import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// https://vitejs.dev/config/
export default defineConfig(() => {
    return {
        plugins: [react()],
        server: {
            host: true,
            port: 80,
            strictPort: true,
            proxy: {
                "/api": {
                    // Docker: http://backend:8080
                    // Local: http://localhost:8080
                    // Local with proxy: not necessary
                    target: "http://localhost:8080",
                    changeOrigin: true,
                    secure: false,
                    rewrite: (path) => path.replace(/^\/api/, ""),
                },
            },
        },
    };
});
