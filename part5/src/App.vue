<template>
    <div id="app">
        <h1>Hello HTML!</h1>

        <p class="description">{{ description }}</p>

        <Counter/>
    </div>
</template>

<script>
    import Counter from './components/Counter.vue'

    export default {
        name: 'App',
        components: {
            Counter: Counter
        },
        data: function () {
            return {
                description: 'HyperText Markup Language'
            }
        }
    }
</script>

<style>
    #app {
        font-family: Avenir, Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        margin-top: 120px;
        text-align: center;
    }

    h1 {
        font-family: "Comic Sans MS", monospace;
        color: darkblue;
    }

    p.description {
        font-style: italic;
        color: darkblue
    }
</style>
