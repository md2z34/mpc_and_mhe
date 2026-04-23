# MPC and MHE
Optimization Model Predictive Control (MPC) and Moving Horizon Estimation (MHE) with CasADi in Python.

## What is an Optimization Problem?
- An objective or cost function $\Phi(\mathbf{w})$ that is minimized or maximized.
- Decision variables $\mathbf{w}$ that are manipulated during the optimization process.
- Equality constraints that shall be respected, $\mathbf{g_1(w)} = 0$.
- Inequality constraints that shall be respected, $\mathbf{g_2(w)} \ge 0$.

## Nonlinear Programming Problem (NLP)
$$
\begin{align*}
\min_w \quad & \Phi(\mathrm{w}), \\
\text{s.t.} \quad & \mathrm{g_1}(\mathrm{w}) = 0, \\
& \mathrm{g_2}(\mathrm{w}) \ge 0.
\end{align*}
$$
