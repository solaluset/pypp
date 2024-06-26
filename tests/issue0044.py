from __future__ import absolute_import, print_function
import unittest
import sys

shouldbe = r'''a1



b1
'''


class runner(object):
    def runTest(self):
        from pypp import CmdPreprocessor
        # failure: p = CmdPreprocessor(['pypp', '--line-directive', '#line',
        # p = CmdPreprocessor(['pypp', '--line-directive', 'nothing',
        # p = CmdPreprocessor(['pypp', '--line-directive', 'None',
        p = CmdPreprocessor(['pypp', '--line-directive', '',
                             '-o', 'tests/issue0044.i',
                             'tests/issue0044.h'])
        with open('tests/issue0044.i', 'rt') as ih:
            output = ih.read()
        if output != shouldbe:
            print("Should be:\n" + shouldbe + "EOF\n", file=sys.stderr)
            print("\nWas:\n" + output + "EOF\n", file=sys.stderr)
        self.assertEqual(p.return_code, 0)
        self.assertEqual(output, shouldbe)


class empty_line_directive(unittest.TestCase, runner):
    pass
