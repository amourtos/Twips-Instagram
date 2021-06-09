from instapy import InstaPy

session = InstaPy(username="twip_the_twipper001", password="&[ypZ8cpy]k-")
session.login()
print(f"{session.username} has logged in. Beginning automated processes.")

session.set_user_interact(amount=100, percentage=100,
                          randomize=True, media="Photo")
session.set_sleep_reduce(1)
session.set_skip_users(skip_private=False)

print(f"Acquiring {session.username} followers")
user_followers = session.grab_followers(
    username="twip_the_twipper001", amount="full")
session.follow_by_list(user_followers)


session.like_by_tags(["programmer", "programming", "developer"], amount=5)
session.set_do_follow(True, percentage=100)
session.set_do_comment(True, percentage=100)
session.set_comments(["Nice!", "Beautiful! :heart_eyes:", "That's so cool!"])


print("Acquiring followers from a specific account.")
user_amourtos = session.grab_followers(username="amourtos", amount="full")
session.follow_by_list(user_amourtos)
