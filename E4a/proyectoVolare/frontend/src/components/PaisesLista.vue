<script setup>
import { ref, onMounted } from "vue";
import { getPaises } from "../api/api.js";

const paises = ref([]);
const cargando = ref(true);

onMounted(async () => {
  try {
    const resp = await getPaises();
    paises.value = resp.data;
  } catch (error) {
    console.error("Error cargando países", error);
  } finally {
    cargando.value = false;
  }
});
</script>

<template>
  <div>
    <h2>Listado de Países (API Django)</h2>
    <p v-if="cargando">Cargando...</p>

    <ul v-else>
      <li
        v-for="pais in paises"
        :key="pais.id_pais"
      >
        <router-link :to="`/paises/${pais.id_pais}`">
          {{ pais.nombre }}
        </router-link>
      </li>
    </ul>
  </div>
</template>
