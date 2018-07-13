from production import AND, OR, NOT, PASS, FAIL, IF, THEN, \
    match, populate, simplify, variables
from zookeeper import ZOOKEEPER_RULES
from functools import reduce

# This function, which you need to write, takes in a hypothesis
# that can be determined using a set of rules, and outputs a goal
# tree of which statements it would need to test to prove that
# hypothesis. Refer to the problem set (section 2) for more
# detailed specifications and examples.

# Note that this function is supposed to be a general
# backchainer.  You should not hard-code anything that is
# specific to a particular rule set.  The backchainer will be
# tested on things other than ZOOKEEPER_RULES.


def backchain_to_goal_tree(rules, hypothesis):
    rule_match = []

    for rule in rules:
        value = match(rule.consequent()[0], hypothesis)
        if value is not None:
            rule_match.append(rule)
            # print rule
        else:
            pass

    if len(rule_match) == 0:
        return hypothesis

    else:
        or_add = OR(hypothesis)
        for rule in rule_match:
            vars = match(rule.consequent()[0], hypothesis)
            if isinstance(rule.antecedent(), OR):
                for idx, ant in enumerate(rule.antecedent()):
                    add_or = backchain_to_goal_tree(
                        rules,  populate(ant, vars))
                    if idx == 0:
                        or_lst = OR(add_or)
                    else:
                        or_lst = OR(or_lst, add_or)
                or_lst = simplify(or_lst)
                or_add = OR(or_add, or_lst)

            elif isinstance(rule.antecedent(), AND):
                for idx, ant in enumerate(rule.antecedent()):
                    add_and = backchain_to_goal_tree(
                        rules,  populate(ant, vars))
                    if idx == 0:
                        and_lst = AND(add_and)
                    else:
                        and_lst = AND(and_lst, add_and)
                and_lst = simplify(and_lst)
                or_add = OR(or_add, and_lst)
            else:
                for idx, ant in enumerate([rule.antecedent()]):
                    add_and = backchain_to_goal_tree(
                        rules,  populate(ant, vars))
                or_add = OR(or_add, add_and)
        return simplify(or_add)


# Here's an example of running the backward chainer - uncomment
# it to see it work:


# backchain_to_goal_tree(ZOOKEEPER_RULES, 'opus is a penguin')

# backchain_to_goal_tree([IF(AND('(?x) has (?y)',
#                                '(?x) has (?z)'),
#                            THEN('(?x) has (?y) and (?z)')),
#                         IF('(?x) has rhythm and music',
#                            THEN('(?x) could not ask for anything more'))],
#                        'gershwin could not ask for anything more')
