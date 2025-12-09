<script setup>
import { computed } from "vue";

const props = defineProps({
  json: {
    type: Object,
    required: true,
  },
});

const jsonString = computed(() => JSON.stringify(props.json));
</script>

<template>
  <!-- usamos <component is="script"> para que Vue no se queje -->
  <component
    :is="'script'"
    type="application/ld+json"
    v-html="jsonString"
  />
</template>
