from ninfo import PluginBase

class shodan_plug(PluginBase):
    """This plugin returns any information from Shodan"""
    name    =    'shodan'
    title   =    'Shodan'
    description   =  'Computer Search Engine'
    cache_timeout   =  60*60*2
    types   =    ['ip','ip6','hostname']
    remote = False

    def setup(self):
        from shodan import WebAPI
        self.api = WebAPI(self.plugin_config["api_key"])

    def get_info(self, arg):
        info = self.api.host(arg)
        return info

plugin_class = shodan_plug
