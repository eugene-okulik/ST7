def cookies_not_empty(driver):
    def _predicate(_):
        return driver.get_cookies() != []

    return _predicate