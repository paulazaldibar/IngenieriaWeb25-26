<script setup>
import { ref, onMounted, computed } from "vue";
import { useRoute } from "vue-router";
import { getAerolinea } from "../api/api.js";
import ShareButtons from "./ShareButtons.vue";
import JsonLd from "./JsonLd.vue";

const route = useRoute();
const aerolinea = ref(null);
const cargando = ref(true);

onMounted(async () => {
  try {
    const id = route.params.id;
    const resp = await getAerolinea(id);
    aerolinea.value = resp.data;
  } catch (error) {
    console.error("Error cargando aerolínea", error);
  } finally {
    cargando.value = false;
  }
});

// URL actual de la página (para compartir)
const currentUrl = computed(() => window.location.href);

// JSON-LD dinámico para esta aerolínea
const jsonLd = computed(() => {
  if (!aerolinea.value) return {};

  return {
    "@context": "https://schema.org",
    "@type": "Airline",
    "name": aerolinea.value.nombre,
    "iataCode": aerolinea.value.siglas,
    "description": aerolinea.value.descripcion,
    "areaServed": aerolinea.value.pais_origen,
    "logo": aerolinea.value.logo || undefined,
  };
});
</script>

<template>
  <div>
    <p v-if="cargando">Cargando aerolínea...</p>

    <article
      v-else-if="aerolinea"
      itemscope
      itemtype="https://schema.org/Airline"
    >
      <h2 itemprop="name">
        Aerolínea: {{ aerolinea.nombre }}
      </h2>

      <p>
        <strong>Siglas:</strong>
        <span itemprop="iataCode">
          {{ aerolinea.siglas }}
        </span>
      </p>

      <p>
        <strong>Descripción:</strong>
        <span itemprop="description">
          {{ aerolinea.descripcion }}
        </span>
      </p>

      <p v-if="aerolinea.pais_origen">
        <strong>País de origen:</strong>
        <span itemprop="areaServed">
          {{ aerolinea.pais_origen }}
        </span>
      </p>

      <div v-if="aerolinea.logo">
        <img
          :src="aerolinea.logo"
          alt="Logo aerolínea"
          itemprop="logo"
          style="max-width: 200px"
        />
      </div>

      <!-- Botones sociales -->
      <ShareButtons
        :url="currentUrl"
        :texto="`Mira esta aerolínea: ${aerolinea.nombre}`"
      />

      <!-- JSON-LD específico de esta aerolínea -->
      <JsonLd :json="jsonLd" />
    </article>

    <p v-else>No se encontró la aerolínea.</p>
  </div>
</template>
