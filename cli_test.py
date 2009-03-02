# coding:utf-8
import unittest
from cli import Cli


class CliTest (unittest.TestCase):

    def test_parameters(self):
        cli = Cli()
        parser = cli.get_parser()
        
        self.assertTrue(parser.has_option("-f"))
        self.assertTrue(parser.has_option("--fullscreen"))
        
        self.assertTrue(parser.has_option("-s"))
        self.assertTrue(parser.has_option("--soundfile"))

        self.assertTrue(parser.has_option("-l"))
        self.assertTrue(parser.has_option("--timeline"))
        
        self.assertTrue(parser.has_option("-t"))
        self.assertTrue(parser.has_option("--text"))

#faz com que a classe saiba que é um teste unitário        
if __name__ == '__main__':
    unittest.main()
