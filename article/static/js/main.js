new Vue({
    el: '#app',
    delimiters: ['${', '}'],
    data: {
        loading: true,
        preview: false,
        
        articles: [],
        currentArticle: {},
        newArticleTemplate: {'title': '', 'content': ''},
        
        search_term: '',
    },
    mounted: function() {
        this.getArticles();
    },
    methods: {
        getArticles: function(withLoading=true) {
            this.loading = withLoading;
            this.$http
                .get(`/api/article/`)
                .then((response) => {
                    this.articles = response.data;
                    this.loading = false;
                })
                .catch((error) => {
                    this.loading = false;
                    console.log(error);
                })
        },
        getArticle: function(id) {
            this.$http
                .get(`/api/article/${id}/`)
                .then((response) => {
                    this.currentArticle = response.data;
                    $("#editArticleModal").modal('show');
                })
                .catch((error) => {
                    console.log(error);
                })
        },
        showArticle: function(id) {
            this.$http
                .get(`/api/article/${id}/`)
                .then((response) => {
                    this.currentArticle = response.data;
                    this.preview = true;
                })
                .catch((error) => {
                    this.preview = false;
                    console.log(error);
                })
        },
        addArticle: function() {
            this.loading = true;
            this.$http
                .post(`/api/article/`, this.newArticleTemplate)
                .then((response) => {
                    this.loading = true;
                    this.getArticles();
                })
                .catch((error) => {
                    this.loading = true;
                    console.log(error);
                })
        },
        updateArticle: function() {
            // this.loading = true;
            this.$http
                .put(`/api/article/${this.currentArticle.id}/`, this.currentArticle)
                .then((response) => {
                    this.loading = false;
                    this.currentArticle = response.data;
                    this.getArticles();
                })
                .catch((error) => {
                    this.loading = false;
                    console.log(error);
                })
        },
        deleteArticle: function(id) {
            // this.loading = true;
            this.$http
                .delete(`/api/article/${id}/`)
                .then((response) => {
                    this.loading = false;
                    this.getArticles(withLoading=false);
                })
                .catch((error) => {
                    this.loading = false;
                    console.log(error);
                })
        }
    }
});
