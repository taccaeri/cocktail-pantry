
<template>
    <div class="cocktails_container">
        <div class="cocktails_content">
            <h1>Tasks</h1>
            <ul class="cocktails_list">
                <li v-for="Cocktail in cocktails" :key="Cocktail.id">
                    <h1>{{ Cocktail.name }}</h1>
                    <h2>{{ Cocktail.bartender }}</h2>
                    <p style="color:green">{{ Cocktail.ingredients }}</p>
                    <p>{{ Cocktail.description }}</p>
                    <p>{{ Cocktail.method }}</p>
                    <button @click="toggleCocktail(Cocktail)">
                        {{ Cocktail.completed ? 'Undo' : 'Complete' }}
                    </button>
                    <button @click="deleteCocktail(Cocktail)">Delete</button>
                </li>
            </ul>
        </div>
    </div>
</template>


<script>
    export default {
        data() {
            return {
                cocktails: ['']
            }
        },
        methods: {
            async getData() {
                try {
                    // fetch cocktails
                    const response = await this.$http.get('http://localhost:8000/cocktails/');
                    // set the data returned as cocktails
                    this.cocktails = response.data;
                } catch (error) {
                    // log the error
                    console.log(error);
                }
            },
        },
        created() {
            // Fetch cocktails on page load
            this.getData();
        }
    }
</script>
