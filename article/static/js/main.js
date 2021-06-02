new Vue({
    el: '#app',
    delimiters: ['${', '}'],
    data: {
        loading: false,
        preview: false,

        page: '/api/article/',
        pages_info: null,

        articles: [],
        currentArticle: {},
        newArticleTemplate: {'title': '', 'content': ''},
        
        search: '',
    },
    mounted: function() {
        this.getArticles();
    },
    watch: {
        page: function() {
            this.page && this.getArticles(this.page, false);
        },
        search: function() {
            value = this.search.trim().toUpperCase();
            this.getArticles(`/api/article/?search=${value}`, false);
        },
    },
    methods: {
        getArticles: function(url=`/api/article/`, withLoading=true) {
            this.loading = withLoading;
            this.$http
                .get(url)
                .then((response) => {
                    this.pages_info = response.data.pages_info;
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
                    this.preview = !this.preview;
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
                    this.getArticles(this.page);
                    this.newArticleTemplate.title = '';
                    this.newArticleTemplate.content = '';
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
                    this.getArticles(this.page);
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
                    this.getArticles(this.page, withLoading=false);
                })
                .catch((error) => {
                    console.log(error);
                })
            this.loading = false;
        }
    }
});
