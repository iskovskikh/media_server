// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    compatibilityDate: '2024-04-03',
    devtools: {enabled: true},

    runtimeConfig: {
        public: {
            // API_BASE_URL: process.env.API_BASE_URL || 'http://localhost:8000/',
            API_BASE_URL:'http://localhost:8000',
        },
    },
    ssr: false
})