window.onload = () => {
    const like_buttons = document.querySelectorAll('[data-operationid="like"]');

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
}