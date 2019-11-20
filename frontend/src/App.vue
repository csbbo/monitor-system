<template>
  <div id="app">
    <app-index></app-index>
  </div>
</template>

<script>
import Index from './components/Index'
export default {
  name: 'app',
  components: {
    "app-index":Index
  }
}
</script>
