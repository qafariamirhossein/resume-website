Vue.component('like', {
    template: "<div class='like-data float-right text-white'><button class='icon-rocknroll mr-1 p-0 border-0' v-class='active: liked' v-on='click: toggleLike'><i class='fa fa-thumbs-up text-white' aria-hidden='true'></i></button><span class='like-count' v-class='active: liked'>{{ likesCount }}</span></div>",
    data: function() {
    return {
    liked: false,
    likesCount: 0
    }
    },
    methods: {
    toggleLike: function() {
    this.liked = !this.liked;
    this.liked ? this.likesCount++ : this.likesCount--;
    }
    }
    });
    new Vue({
    el: '.comments-main',
    });