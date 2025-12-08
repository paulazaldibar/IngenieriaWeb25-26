<template>
  <div class="app">
    <header class="app-header">
      <h1>Proyecto Volare - SPA Vue</h1>
    </header>

    <nav class="app-nav">
      <router-link to="/aerolineas">Aerolíneas</router-link>
      <router-link to="/paises">Países</router-link>
      <router-link to="/aeropuertos">Aeropuertos</router-link>
    </nav>

    <main class="app-main">
      <router-view />
    </main>
  </div>
</template>

<script setup>
</script>

<style>
/* ==== Estilos globales básicos ==== */
* {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI",
    sans-serif;
  background: #f3f4f6;
}

/* Contenedor principal */
.app {
  min-height: 100vh;
}

/* Header */
.app-header {
  background: #1f2933;
  color: #ffffff;
  padding: 1rem 2rem;
}

.app-header h1 {
  margin: 0;
  font-size: 1.6rem;
}

/* Navegación */
.app-nav {
  background: #e5e7eb;
  padding: 0.75rem 2rem;
}

.app-nav a {
  margin-right: 1rem;
  text-decoration: none;
  color: #0366d6;
  font-weight: 500;
}

.app-nav a.router-link-active {
  font-weight: 700;
  text-decoration: underline;
}

/* Contenido principal */
.app-main {
  padding: 2rem;
}

/* Listas y detalle */
h2 {
  margin-top: 0;
}

ul {
  list-style: none;
  padding-left: 0;
}

li {
  margin-bottom: 0.5rem;
}

a {
  color: #0366d6;
}

a:hover {
  text-decoration: underline;
}

/* Imágenes en detalle */
img {
  border-radius: 6px;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.12);
}
</style>
