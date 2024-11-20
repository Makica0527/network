const { response } = require("express");

document.addEventListener('DOMContentLoaded', function() { 
    post_form = document.querySelector('#post-form');
    post_form.addEventListener('submit', (event) => {
        event.preventDefault();
        uploadPosts();
    });
})

function fetchPosts() {
    fetch('/get_posts')
       .then(response => response.json())
       .then(posts => {
            // Display posts in the UI
            for (const post of posts) {
                const tweetContainer = document.createElement('div');
                tweetContainer.className = 'tweet-container';
                if (post.media != null){
                    const mediaExtension = mediaUrl.split('.').pop().toLowerCase();
                    const imageExtensions = ["jpg", "jpeg", "png", "gif", "bmp", "webp"];
                    const videoExtensions = ["mp4", "webm", "ogg"];

                    if (imageExtensions.includes(mediaExtension)) {
                        mediaContent = `<img src="${mediaUrl}" alt="Tweet image">`;
                    } else if (videoExtensions.includes(mediaExtension)) {
                        mediaContent = `<video controls src="${mediaUrl}"></video>`;
                    } else {
                        mediaContent = '<p>Unsupported media format</p>';
                    }
                    tweetContainer.innerHTML = `
                    <div class="tweet-header">
                        <div class="avatar"></div>
                        <div class="tweet-user-info">
                            <div class="tweet-username">${post.creator}</div>
                            <div>
                                <span class="tweet-handle">${post.creator}</span>
                                <span class="tweet-date">${post.date}</span>
                            </div>
                        </div>
                    </div>
                    <div class="tweet-content">${post.caption}</div>
                    <div class="tweet-media">${post.media}</div>
                    <div class="tweet-reply"></div>`
                }else{
                    tweetContainer.innerHTML = `
                    <div class="tweet-header">
                        <div class="avatar"></div>
                        <div class="tweet-user-info">
                            <div class="tweet-username">${post.creato}</div>
                            <div>
                                <span class="tweet-handle">${post.creato}</span>
                                <span class="tweet-date">${post.date}</span>
                            </div>
                        </div>
                    </div>
                    <div class="tweet-content">${post.caption}</div>
                    <div class="tweet-reply"></div>
                `
                }
                ;

                document.getElementById('post-home-page-conatainer').appendChild(tweetContainer);
            }
        })
       .catch(error => {
            console.error('Error:', error);
        });
}

function uploadPosts() {

    const message = document.querySelector("#post-form-msg").value;
    const file = fileInput.files[0]; // Get the first selected file

    const formData = new FormData();
    formData.append("message", message);
    if (file) {
        formData.append("file", file);
    }

    fetch('/new_post', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCsrfToken() // if CSRF protection is enabled
        },
        body: formData
    })
    .then(response => response.json())
    .then(result => {
        if (result.status === 'success') {
            const post = result.post;
            addTweet(post.username, post.handle, post.date, post.content, post.mediaUrl);
        } else {
            console.error('Error uploading post:', result.message);
        }
    })
    .catch(error => console.error('Error:', error));
}

// Helper function to get CSRF token if CSRF protection is enabled
function getCsrfToken() {
    const name = 'csrftoken';
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.startsWith(name + '=')) {
            return decodeURIComponent(cookie.substring(name.length + 1));
        }
    }
    return '';
}