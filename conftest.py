import os

from hypothesis import Settings, Verbosity


Settings.register_profile("dev", Settings(max_examples=10))
Settings.register_profile(
    "debug",
    Settings(max_examples=10, verbosity=Verbosity.verbose),
)
Settings.load_profile(os.getenv(u'HYPOTHESIS_PROFILE', 'dev'))
