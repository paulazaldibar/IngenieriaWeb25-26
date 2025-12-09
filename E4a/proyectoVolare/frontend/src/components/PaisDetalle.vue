<script setup>
import { ref, onMounted, computed } from "vue";
import { useRoute } from "vue-router";
import { getPais } from "../api/api.js";
import ShareButtons from "./ShareButtons.vue";
import JsonLd from "./JsonLd.vue";

const route = useRoute();
const pais = ref(null);
const cargando = ref(true);

onMounted(async () => {
  try {
    const id = route.params.id;
    const resp = await getPais(id);
    pais.value = resp.data;
  } catch (error) {
    console.error("Error cargando país", error);
  } finally {
    cargando.value = false;
  }
});

// URL actual para compartir
const currentUrl = computed(() => window.location.href);

// JSON-LD dinámico
const jsonLd = computed(() => {
  if (!pais.value) return {};

  return {
    "@context": "https://schema.org",
    "@type": "Country",
    "name": pais.value.nombre,
    "description": pais.value.curiosidad,
    "image": pais.value.bandera || undefined,
  };
});
</script>

<template>
  <div>
    <p v-if="cargando">Cargando país...</p>

    <article
      v-else-if="pais"
      itemscope
      itemtype="https://schema.org/Country"
    >
      <h2 itemprop="name">País: {{ pais.nombre }}</h2>

      <p>
        <strong>Curiosidad:</strong>
        <span itemprop="description">{{ pais.curiosidad }}</span>
      </p>

      <div v-if="pais.bandera">
        <img
          :src="pais.bandera"
          alt="Bandera"
          itemprop="image"
          style="max-width: 200px; margin-top: 10px"
        />
      </div>

      <!-- Botones sociales -->
      <ShareButtons
        :url="currentUrl"
        :texto="`Mira este país: ${pais.nombre}`"
      />

      <!-- JSON-LD dinámico -->
      <JsonLd :json="jsonLd" />
    </article>

    <p v-else>No se encontró el país.</p>
  </div>
</template>
