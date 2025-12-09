<script setup>
const props = defineProps({
  url: {
    type: String,
    required: true,
  },
  texto: {
    type: String,
    required: true,
  },
});
</script>

<template>
  <div class="share-buttons">
    <span>Compartir:</span>

    <a
      :href="`https://twitter.com/intent/tweet?url=${encodeURIComponent(url)}&text=${encodeURIComponent(texto)}`"
      target="_blank"
      rel="noopener noreferrer"
    >
      Twitter
    </a>

    <a
      :href="`https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(url)}`"
      target="_blank"
      rel="noopener noreferrer"
    >
      Facebook
    </a>
  </div>
</template>

<style scoped>
.share-buttons {
  margin-top: 1rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.share-buttons a {
  text-decoration: none;
  font-size: 0.9rem;
  color: #0366d6;
}

.share-buttons a:hover {
  text-decoration: underline;
}
</style>
