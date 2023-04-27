from django.conf import settings  # import the settings file


def testing_feature_flag(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return {"testing_feature_flag": settings.TESTING_FEATURE_FLAG}
