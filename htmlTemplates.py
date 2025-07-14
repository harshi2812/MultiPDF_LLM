# htmlTemplates.py (Updated with better CSS and local images)

css = '''
<style>
body {
    background-color: #f0f2f5;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.chat-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 2rem;
}

.chat-message {
    padding: 1.2rem;
    border-radius: 1rem;
    margin: 1rem 0;
    display: flex;
    align-items: flex-start;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    transition: all 0.3s ease-in-out;
    background: linear-gradient(to right, #6a11cb 0%, #2575fc 100%);
    color: white;
}

.chat-message.user {
    background: linear-gradient(to right, #00c6ff, #0072ff);
    justify-content: flex-end;
    flex-direction: row-reverse;
    text-align: right;
}

.chat-message .avatar {
    width: 50px;
    height: 50px;
    margin: 0 1rem;
}

.chat-message .avatar img {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    border: 2px solid white;
    object-fit: cover;
}

.chat-message .message {
    max-width: 70%;
    font-size: 1.1rem;
    line-height: 1.5;
    word-wrap: break-word;
}
</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <a href="images/image2.png" target="_blank">
            <img src="images/image2.png" alt="Bot Avatar">
        </a>
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''


user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <a href="images/image1.png" target="_blank">
            <img src="images/image1.png" alt="User Avatar">
        </a>
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''

