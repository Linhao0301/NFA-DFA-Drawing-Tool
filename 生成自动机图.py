from graphviz import Digraph

#画图结构有一定随机性，如果不好看的话可以尝试多生成几次
def draw(states, transitions, start_state, accept_states):
    dot = Digraph(engine='dot')  # 选择布局算法


    # 添加所有状态
    for state in states:
        if state in accept_states:
            dot.node(state, state, shape='doublecircle')
        else:
            dot.node(state, state, shape='circle')

    # 添加初始状态指示器
    dot.node('', shape='plaintext')
    dot.edge('', start_state, label='start')

    # 添加转换
    for start, end, symbol in transitions:
        dot.edge(start, end, label=symbol)

    # 你可以根据你是在绘制NFA还是DFA来选择合适的文件名
    dot.render('NFA or DFA', format='png', cleanup=True)  # 更改文件名以反映你是在绘制NFA
    return dot

# 状态集，确保包括了所有的状态
states = {'α', 'β', 'ψ', 'δ'}
# 转换，格式为(start_state, end_state, symbol)
transitions = {
    ('α', 'β', 'a'),
    ('α', 'α', 'b'),
    ('β', 'β', 'a'),
    ('β', 'ψ', 'b'),
    ('ψ', 'β', 'a'),
    ('ψ', 'δ', 'b'),
    ('δ', 'δ', 'a'),
    ('δ', 'δ', 'b'),

}
# 开始状态
start_state = 'α'
# 接受状态集
accept_states = {'δ'}

draw(states, transitions, start_state, accept_states)
