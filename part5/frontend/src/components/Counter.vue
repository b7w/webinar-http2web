<template>
    <div>
        <p v-show="loading === false">{{ counter }}</p>

        <button v-show="loading === false" v-on:click="increment()">Increment</button>
    </div>
</template>

<script>
    export default {
        name: 'Counter',
        data: function () {
            return {
                loading: true,
                counter: 0
            }
        },
        mounted: function () {
            this.init();
        },
        methods: {
            init: function () {
                fetch('/api/counter')
                        .then(response => response.text())
                        .then(text => {
                            this.counter = text;
                            this.loading = false;
                        })
            },
            increment: function () {
                fetch('/api/increment')
                        .then(response => response.text())
                        .then(text => {
                            this.counter = text;
                        })
            }
        }
    }
</script>

<style scoped>
    p {
        color: darkred;
    }
</style>
