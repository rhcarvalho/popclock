# coding:utf-8
import unittest
from cli import Cli


class CliTest (unittest.TestCase):

    def test_parameters(self):
        cli = Cli()
        parser = cli.get_parser()

        self.assertTrue(parser.has_option("-m"))
        self.assertTrue(parser.has_option("--message"))

        self.assertTrue(parser.has_option("-s"))
        self.assertTrue(parser.has_option("--soundfile"))

        self.assertTrue(parser.has_option("-e"))
        self.assertTrue(parser.has_option("--exitat"))

        self.assertTrue(parser.has_option("-t"))
        self.assertTrue(parser.has_option("--timeline"))

        self.assertTrue(parser.has_option("-f"))
        self.assertTrue(parser.has_option("--fullscreen"))

        self.assertTrue(parser.has_option("-a"))
        self.assertTrue(parser.has_option("--alarm"))

    def test_defaults(self):
        cli = Cli()
        (opt,vls) = cli.parse()

        self.assertEquals(opt.message,'')
        self.assertEquals(opt.soundfile,None)
        self.assertEquals(opt.exitat,5)
        self.assertEquals(opt.timeline,False)
        self.assertEquals(opt.fullscreen,False)
        self.assertEquals(opt.alarm,False)

    def test_if_have_just_that_options(self):
        cli = Cli()
        (opt,vls) = cli.parse()

        #FIXME: need to find another way to test if 'Cli' just have that options
        self.assertEquals(opt,{'fullscreen': False,
                               'message': '',
                               'exitat': 5,
                               'soundfile': None,
                               'timeline': False,
                               'debug': False,
                               'alarm': False})


#faz com que a classe saiba que é um teste unitário        
if __name__ == '__main__':
    unittest.main()
