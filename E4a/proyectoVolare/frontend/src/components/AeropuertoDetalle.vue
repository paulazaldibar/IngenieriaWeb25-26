<script setup>
import { ref, onMounted, computed } from "vue";
import { useRoute } from "vue-router";
import { getAeropuerto } from "../api/api.js";
import ShareButtons from "./ShareButtons.vue";
import JsonLd from "./JsonLd.vue";

const route = useRoute();
const aeropuerto = ref(null);
const cargando = ref(true);

onMounted(async () => {
  try {
    const id = route.params.id;
    const resp = await getAeropuerto(id);
    aeropuerto.value = resp.data;
  } catch (error) {
    console.error("Error cargando aeropuerto", error);
  } finally {
    cargando.value = false;
  }
});

// URL actual para compartir
const currentUrl = computed(() => window.location.href);

// JSON-LD dinámico
const jsonLd = computed(() => {
  if (!aeropuerto.value) return {};

  return {
    "@context": "https://schema.org",
    "@type": "Airport",
    "name": aeropuerto.value.nombre,
    "iataCode": aeropuerto.value.siglas,
    "address": aeropuerto.value.pais,
    "image": aeropuerto.value.foto || undefined,
  };
});
</script>

<template>
  <div>
    <p v-if="cargando">Cargando aeropuerto...</p>

    <article
      v-else-if="aeropuerto"
      itemscope
      itemtype="https://schema.org/Airport"
    >
      <h2 itemprop="name">Aeropuerto: {{ aeropuerto.nombre }}</h2>

      <p>
        <strong>Siglas:</strong>
        <span itemprop="iataCode">{{ aeropuerto.siglas }}</span>
      </p>

      <p>
        <strong>País:</strong>
        <span itemprop="address">{{ aeropuerto.pais }}</span>
      </p>

      <div v-if="aeropuerto.foto">
        <img
          :src="aeropuerto.foto"
          alt="Foto aeropuerto"
          itemprop="image"
          style="max-width: 300px; margin-top: 10px"
        />
      </div>

      <!-- Botones sociales -->
      <ShareButtons
        :url="currentUrl"
        :texto="`Mira este aeropuerto: ${aeropuerto.nombre}`"
      />

      <!-- JSON-LD dinámico -->
      <JsonLd :json="jsonLd" />
    </article>

    <p v-else>No se encontró el aeropuerto.</p>
  </div>
</template>
