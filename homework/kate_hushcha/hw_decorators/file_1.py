
def the_end(finished):

    def wrapper(*args, **kwargs):
        finished(*args, **kwargs)
        print('finished')

    return wrapper


@the_end
def story(words):
    print(words)


story('Many many years ago...')
