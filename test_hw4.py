import unittest
import hw4


class StackTest(unittest.TestCase):
    def test_stackpush(self):
        actual = hw4.Stack()
        actual.push('Camus'), actual.push('Sartre')
        expected = ['Camus', 'Sartre']
        self.assertListEqual(actual.elements, expected)

    def test_stackpop(self):
        actual = hw4.Stack()
        self.assertEqual(actual.pop(), None)


class QueueTest(unittest.TestCase):
    def test_queueadd(self):
        actual = hw4.Queue()
        actual.add('Olga')
        expected = ['Olga']
        self.assertListEqual(actual.queue, expected)

    def test_queueremove(self):
        actual = hw4.Queue()
        self.assertEqual(actual.remove(), None)

    def test_queuesize(self):
        initial = hw4.Queue()
        self.assertEqual(initial.size(), 0)


class ListTest(unittest.TestCase):
    def test_append(self):
        actual = hw4.LinkedList()
        actual.append('a')
        self.assertEqual(str(actual), 'a,None')

    def test_len(self):
        actual = hw4.LinkedList()
        self.assertEqual(len(actual), 0)

    def test_repr(self):
        actual = hw4.LinkedList()
        self.assertFalse(actual, None)


if __name__ == "__main__":
  unittest.main()
