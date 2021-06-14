<template>
  <div class="hello">
      <h1> List locations and defects</h1>
        <input id = "get-locations"
        v-model="search_phrase"
        placeholder = "searchphrase"
        @keyup = "fetchAPILocations">
        <ul>
            <li v-for='location in locations_sliced' :key="location.location_name ">{{ location.location_name }}</li>
        </ul>

        <button type = "button"
        id = "get-locations"
        @click = "fetchAPIDefects">Get defects</button>
        <!-- comment -->
        <ul>
            <li v-for='defect in defects' :key="defect.defect_name">{{ defect.defect_name }}  </li>
        </ul>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data() {
        return {
            locations: [],
            defects: [],
            search_phrase: '',
        }
},
// computed functions will be run when  
computed: {
locations_sliced() {
    return this.locations.slice(0,3);
}
},
mounted() {

setTimeout(() => {
    console.log('hello', this.locations);
}, 600);
},

    methods: {
        fetchAPILocations() {
            this.responseAvailable = false;
            // a url should be stored as a variable or in a file
            // axios - better way to access api data
            fetch(`http://127.0.0.1:8000/api/location-detail/?search=${this.search_phrase}`, {
                "method": "GET",
            })
                .then(response => {
                    if (response.ok) {
                        return response.json()
                    } else {
                        alert("Server returned " + response.status + " : " + response.statusText);
                    }
                })
                .then(response => {
                    this.locations = response;
                })
                .catch(err => {
                    console.log(err);
                });
        },
        fetchAPIDefects() {
            this.responseAvailable = false;
            fetch("http://127.0.0.1:8000/api/defects-detail/", {
                "method": "GET",
            })
            // DRY - make small functions that can be used in multiple places
                .then(response => {
                    if (response.ok) {
                        return response.json();
                    } else {
                        alert("Server returned " + response.status + " : " + response.statusText);
                    }
                })
                .then(response => {
                    console.log(response);
                    this.defects = response.results;
                })
                .catch(err => {
                    console.log(err);
                });
        }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
