from django.shortcuts import render
from datetime import date

all_posts = [
    {
        "post_identifier": "skating2",
        "image": "thumb-1920-600459.jpg",
        "author": "Akash",
        "date": date(2024, 3, 16),
        "title": "Skating2!",
        "excerpt": "Says random stuff about skating and stuff",
        "content": """
            Quas tempora delectus eaque officiis optio recusandae nihil quia assumenda, asperiores iste a distinctio repudiandae esse error atque iure expedita amet, facere autem nemo commodi repellendus a voluptatem aut expedita accusantium assumenda, omnis dolorem magnam veniam consectetur minima officia impedit accusantium eius facere? Saepe sequi vel recusandae consequatur consequuntur labore similique, doloribus natus ullam in, quae eum voluptatum eveniet a deserunt. Provident eius perspiciatis quisquam natus rem cupiditate, delectus illum eos iste repellendus corporis laboriosam laborum fuga quam rerum ex, vitae assumenda veniam. Amet perspiciatis cupiditate provident in id, harum praesentium quia odio corrupti culpa eligendi tempora debitis, distinctio ipsa voluptas perspiciatis est similique eum, corrupti odio beatae officia sapiente natus nostrum dolorem voluptatem assumenda.

            Necessitatibus sit velit illum pariatur provident vero ratione reprehenderit corrupti, voluptatibus tempora dolore cumque inventore mollitia error sapiente, fugit tempore voluptatibus repellendus ipsa quasi pariatur deserunt magnam ipsam, quidem inventore nostrum aliquam quam distinctio deserunt, eos dignissimos impedit libero enim et? Sit optio neque unde sunt est porro error voluptas, aliquam sapiente nesciunt laboriosam earum expedita dolorem mollitia ut excepturi. Voluptatum dolor architecto sunt beatae, vel voluptatibus id, a dignissimos sunt dolore itaque ad similique aspernatur? Nisi reprehenderit eos magni excepturi dolor deserunt dolorum, aliquid beatae laborum amet ducimus similique excepturi esse accusamus dignissimos maiores.

            Autem qui in animi rem accusantium explicabo, voluptatibus eius quo perferendis soluta temporibus nihil? Iusto eos asperiores velit blanditiis reprehenderit ea atque natus incidunt aliquam quam, facere aspernatur maiores sapiente neque necessitatibus saepe, corporis quisquam dolores cum quis, repellat laboriosam optio maiores unde laborum quisquam quo, quo neque vel possimus nesciunt libero officia? Fugit fuga laborum maiores quas, cupiditate minus eius atque totam accusantium earum repudiandae amet odit. Molestias id magni, officiis ullam aliquid iure quaerat modi assumenda, deserunt rem autem ex non?

            Iure magni vitae facilis veniam excepturi rerum repellat provident maxime, unde culpa assumenda voluptatum distinctio, error voluptate ipsum sunt, assumenda commodi tempora voluptas officiis libero, exercitationem consectetur natus cumque suscipit? Recusandae optio eos aperiam consequuntur.

            Alias similique ea corrupti, nostrum repudiandae quos eaque repellat dolor minus pariatur adipisci voluptate error?
            """,
    },
    {
        "post_identifier": "skating1",
        "image": "thumb-1920-600459.jpg",
        "author": "Akash",
        "date": date(2024, 3, 13),
        "title": "Skating1!",
        "excerpt": "Says random stuff about skating and stuff",
        "content": """
            Quas tempora delectus eaque officiis optio recusandae nihil quia assumenda, asperiores iste a distinctio repudiandae esse error atque iure expedita amet, facere autem nemo commodi repellendus a voluptatem aut expedita accusantium assumenda, omnis dolorem magnam veniam consectetur minima officia impedit accusantium eius facere? Saepe sequi vel recusandae consequatur consequuntur labore similique, doloribus natus ullam in, quae eum voluptatum eveniet a deserunt. Provident eius perspiciatis quisquam natus rem cupiditate, delectus illum eos iste repellendus corporis laboriosam laborum fuga quam rerum ex, vitae assumenda veniam. Amet perspiciatis cupiditate provident in id, harum praesentium quia odio corrupti culpa eligendi tempora debitis, distinctio ipsa voluptas perspiciatis est similique eum, corrupti odio beatae officia sapiente natus nostrum dolorem voluptatem assumenda.

            Necessitatibus sit velit illum pariatur provident vero ratione reprehenderit corrupti, voluptatibus tempora dolore cumque inventore mollitia error sapiente, fugit tempore voluptatibus repellendus ipsa quasi pariatur deserunt magnam ipsam, quidem inventore nostrum aliquam quam distinctio deserunt, eos dignissimos impedit libero enim et? Sit optio neque unde sunt est porro error voluptas, aliquam sapiente nesciunt laboriosam earum expedita dolorem mollitia ut excepturi. Voluptatum dolor architecto sunt beatae, vel voluptatibus id, a dignissimos sunt dolore itaque ad similique aspernatur? Nisi reprehenderit eos magni excepturi dolor deserunt dolorum, aliquid beatae laborum amet ducimus similique excepturi esse accusamus dignissimos maiores.

            Autem qui in animi rem accusantium explicabo, voluptatibus eius quo perferendis soluta temporibus nihil? Iusto eos asperiores velit blanditiis reprehenderit ea atque natus incidunt aliquam quam, facere aspernatur maiores sapiente neque necessitatibus saepe, corporis quisquam dolores cum quis, repellat laboriosam optio maiores unde laborum quisquam quo, quo neque vel possimus nesciunt libero officia? Fugit fuga laborum maiores quas, cupiditate minus eius atque totam accusantium earum repudiandae amet odit. Molestias id magni, officiis ullam aliquid iure quaerat modi assumenda, deserunt rem autem ex non?

            Iure magni vitae facilis veniam excepturi rerum repellat provident maxime, unde culpa assumenda voluptatum distinctio, error voluptate ipsum sunt, assumenda commodi tempora voluptas officiis libero, exercitationem consectetur natus cumque suscipit? Recusandae optio eos aperiam consequuntur.

            Alias similique ea corrupti, nostrum repudiandae quos eaque repellat dolor minus pariatur adipisci voluptate error?
            """,
    },
    {
        "post_identifier": "skating3",
        "image": "thumb-1920-600459.jpg",
        "author": "Akash",
        "date": date(2024, 3, 14),
        "title": "Skating3!",
        "excerpt": "Says random stuff about skating and stuff",
        "content": """
            Quas tempora delectus eaque officiis optio recusandae nihil quia assumenda, asperiores iste a distinctio repudiandae esse error atque iure expedita amet, facere autem nemo commodi repellendus a voluptatem aut expedita accusantium assumenda, omnis dolorem magnam veniam consectetur minima officia impedit accusantium eius facere? Saepe sequi vel recusandae consequatur consequuntur labore similique, doloribus natus ullam in, quae eum voluptatum eveniet a deserunt. Provident eius perspiciatis quisquam natus rem cupiditate, delectus illum eos iste repellendus corporis laboriosam laborum fuga quam rerum ex, vitae assumenda veniam. Amet perspiciatis cupiditate provident in id, harum praesentium quia odio corrupti culpa eligendi tempora debitis, distinctio ipsa voluptas perspiciatis est similique eum, corrupti odio beatae officia sapiente natus nostrum dolorem voluptatem assumenda.

            Necessitatibus sit velit illum pariatur provident vero ratione reprehenderit corrupti, voluptatibus tempora dolore cumque inventore mollitia error sapiente, fugit tempore voluptatibus repellendus ipsa quasi pariatur deserunt magnam ipsam, quidem inventore nostrum aliquam quam distinctio deserunt, eos dignissimos impedit libero enim et? Sit optio neque unde sunt est porro error voluptas, aliquam sapiente nesciunt laboriosam earum expedita dolorem mollitia ut excepturi. Voluptatum dolor architecto sunt beatae, vel voluptatibus id, a dignissimos sunt dolore itaque ad similique aspernatur? Nisi reprehenderit eos magni excepturi dolor deserunt dolorum, aliquid beatae laborum amet ducimus similique excepturi esse accusamus dignissimos maiores.

            Autem qui in animi rem accusantium explicabo, voluptatibus eius quo perferendis soluta temporibus nihil? Iusto eos asperiores velit blanditiis reprehenderit ea atque natus incidunt aliquam quam, facere aspernatur maiores sapiente neque necessitatibus saepe, corporis quisquam dolores cum quis, repellat laboriosam optio maiores unde laborum quisquam quo, quo neque vel possimus nesciunt libero officia? Fugit fuga laborum maiores quas, cupiditate minus eius atque totam accusantium earum repudiandae amet odit. Molestias id magni, officiis ullam aliquid iure quaerat modi assumenda, deserunt rem autem ex non?

            Iure magni vitae facilis veniam excepturi rerum repellat provident maxime, unde culpa assumenda voluptatum distinctio, error voluptate ipsum sunt, assumenda commodi tempora voluptas officiis libero, exercitationem consectetur natus cumque suscipit? Recusandae optio eos aperiam consequuntur.

            Alias similique ea corrupti, nostrum repudiandae quos eaque repellat dolor minus pariatur adipisci voluptate error?
            """,
    },
]


# Create your views here.
def index(request):
    sorted_posts = sorted(all_posts, key=lambda x: x["date"], reverse=True)
    latest_posts = sorted_posts[:3]
    return render(
        request,
        "blog/index.html",
        {
            "posts": latest_posts,
        },
    )


def posts(request):
    return render(
        request,
        "blog/all-posts.html",
        {
            "all_posts": all_posts,
        },
    )


def post_details(request, post_identifier):
    identified_post = next(
        post for post in all_posts if post["post_identifier"] == post_identifier
    )
    return render(request, "blog/post-detail.html", {"post": identified_post})
