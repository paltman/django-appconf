from appconf import AppConf

class TestConf(AppConf):

    SIMPLE_VALUE = True

    CONFIGURED_VALUE = 'wrong'

    def configure_configured_value(self, value):
        return 'correct'

    def configure(self):
        self.configured_data['CONFIGURE_METHOD_VALUE'] = True
        return self.configured_data


class PrefixConf(TestConf):

    class Meta:
        app_label = 'prefix'


class YetAnotherPrefixConf(PrefixConf):

    SIMPLE_VALUE = False

    class Meta:
        app_label = 'yetanother_prefix'


class SeparateConf(AppConf):

    SEPARATE_VALUE = True

    class Meta(PrefixConf.Meta):
        pass
