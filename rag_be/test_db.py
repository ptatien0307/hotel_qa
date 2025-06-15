from services.user_service import UserService
from services.session_service import SessionService
user_service = UserService()

# user1 = {
#     'username': 'ptatien',
#     'password': '1597532684'
# }
# user_service.create_user(user1)

user_data = user_service.find_user('ptatien')

session_service = SessionService()

session1 = {
    'user_id': user_data.get('_id'),
    'history': [
        "Lorem ipsum dolor sit amet",
        "consectetur adipiscing elit. Pellentesque quis iaculis ligula. Proin suscipit auctor ipsum, sed gravida urna eleifend eu. In quam enim, sodales in neque eget, malesuada congue neque.",
        "Suspendisse sit amet arcu pellentesque",
        "Sed porttitor leo tincidunt orci iaculis porttitor. Mauris hendrerit luctus mi, ornare eleifend orci feugiat eget. Vestibulum tempus pellentesque tellus, eget facilisis libero consectetur sed",
        "Praesent ultrices eros hendrerit nunc mattis auctor",
        "Pellentesque volutpat imperdiet arcu, maximus fringilla justo suscipit eu. Pellentesque tincidunt mattis leo, at dignissim odio faucibus ac. Integer dictum, nisl non porttitor dignissim, turpis risus consectetur libero, eu maximus odio mi vel nunc. Nulla mattis, diam at accumsan lacinia, lectus nibh porta lorem, quis aliquam purus elit eget quam.",
        "Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae",
        "Ut convallis aliquam elit, ut vehicula elit vestibulum in. Fusce rhoncus lacus quis semper elementum. Pellentesque fermentum auctor diam non iaculis. Nullam vitae lacus eu justo facilisis ullamcorper id vitae justo. Fusce cursus turpis magna, eu aliquam erat volutpat eu",
    ]
}

session_service.create_session(session1)