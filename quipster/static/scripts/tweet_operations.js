window.onload = () => {
    const like_buttons = document.querySelectorAll('[data-operationid="like"]');
    const follow_button = document.querySelector('#follow-button');

    like_buttons.forEach(btn => {
        btn.addEventListener('click', async () => {
            const tweetId = btn.getAttribute('data-tweetid');
            const likeCount = btn.querySelector('p');

            const response = await fetch(`/api/like`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrfToken,
                },
                body: JSON.stringify({ tweet_id: parseInt(tweetId) }),
            });

            if (response.ok) {
                const data = await response.json();

                likeCount.textContent = data.like_count;

                if (data.is_liked) {
                    btn.classList.add('text-[#f91880]');
                } else {
                    btn.classList.remove('text-[#f91880]');
                }
            }
        });
    });

    async function follow(uid) {
        const response = await fetch(`/api/follow`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrfToken,
            },
            body: JSON.stringify({ uid: parseInt(uid) }),
        });

        return response;
    }

    async function unfollow(uid) {
        const response = await fetch(`/api/unfollow`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrfToken,
            },
            body: JSON.stringify({ uid: parseInt(uid) }),
        });
        
        return response;
    }
    
    follow_button?.addEventListener("click", async () => {
        const uid = follow_button.getAttribute('data-uid');
        const followers_count = document.getElementById("followers-count");
        const operation = follow_button.getAttribute("data-operationid");

        if (!operation) return;
        
        const response = (operation == "follow") ? await follow(uid) : await unfollow(uid);

        if (response.ok) {
            const data = await response.json();

            followers_count.textContent = data.followers_count;
            follow_button.textContent = (operation === "follow") ? "" : "Takip et";

            if (operation === "follow") {
                follow_button.setAttribute("data-operationid", "unfollow");
                follow_button.classList.replace("follow", "unfollow");
            } else {
                follow_button.setAttribute("data-operationid", "follow");
                follow_button.classList.replace("unfollow", "follow");
            }
        }
    });
}