new Vue({
    el: '#app',
    delimiters: ['${', '}'],
    data: {
        loading: false,
        preview: false,

        page: 1,
        page_count: 0,

        articles: [],
        currentArticle: {},
        newArticleTemplate: {'title': '', 'content': ''},
        
        search_term: '',
    },
    mounted: function() {
        this.getArticles();
    },
    watch: {
        page () {
            this.page && this.getArticles(`/api/article/?page=${this.page}`, false);
        }
    },
    methods: {
        getArticles: function(url=`/api/article/`, withLoading=true) {
            this.loading = withLoading;
            this.$http
                .get(url)
                .then((response) => {
                    this.page_count = response.data.page_count;
                    this.articles = response.data.articles;
                })
                .catch((error) => {
                    console.log(error);
                })
            this.loading = false;
            this.preview = false;
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
                    this.getArticles();
                })
                .catch((error) => {
                    console.log(error);
                })
        },
        updateArticle: function() {
            // this.loading = true;
            this.$http
                .put(`/api/article/${this.currentArticle.id}/`, this.currentArticle)
                .then((response) => {
                    this.currentArticle = response.data;
                    this.getArticles();
                })
                .catch((error) => {
                    console.log(error);
                })
            this.loading = false;
        },
        deleteArticle: function(id) {
            // this.loading = true;
            this.$http
                .delete(`/api/article/${id}/`)
                .then((response) => {
                    this.getArticles(withLoading=false);
                })
                .catch((error) => {
                    console.log(error);
                })
            this.loading = false;
        }
    }
});
