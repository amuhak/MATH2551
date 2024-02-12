$\displaystyle \lim_{\left(x,y\right)\rightarrow\left(x_0,y_0\right)}f\left(x,y\right)=L$ if for every ε>0, there exists a corresponding δ>0, such that for all $\left(x,y\right)$ in the domain of f, $\left|f\left(x,y\right)-L\right|<\epsilon$ whenever  $0<\sqrt{(x-x_0)^2+(y-y_0)^2}<\delta$

$\displaystyle \frac{\partial f}{\partial x}|_{\left(x_0,y_0\right)}=\lim_{h\rightarrow0}\frac{f\left(x_0+h,y_0\right)-f\left(x_0,y_0\right)}{h}=f_x\left(x_0,y_0\right)$

$$\begin{aligned}
f_{xx}&=\frac{\partial^2f}{\partial x^2}=\frac{\partial}{\partial x}\left(\frac{\partial f}{\partial x}\right)\\
f_{yy}&=\frac{\partial^2f}{\partial y^2}=\frac{\partial}{\partial y}\left(\frac{\partial f}{\partial y}\right)\\
f_{xy}&=\frac{\partial^2f}{\partial yx}=\frac{\partial}{\partial y}\left(\frac{\partial f}{\partial x}\right)\\
f_{yx}&=\frac{\partial^2f}{\partial xy}=\frac{\partial}{\partial x}\left(\frac{\partial f}{\partial y}\right)\\
\frac{dw}{dt}&=\frac{\partial w}{\partial x}\cdot\frac{dx}{dt}+\frac{\partial w}{\partial y}\cdot\frac{dy}{dt}+\frac{\partial w}{\partial z}\cdot\frac{dz}{dt}\\
\frac{dy}{dx}&=-\frac{F_x}{F_y}
\end{aligned}
$$
Directional Derivative of the unit vector $u = u_1 \mathbf{i} + u_2 \mathbf{j}$
$$
\begin{align*}
f'_u\left(x,y\right)=D_uf\left(x,y\right)&=\lim_{s\rightarrow0}\frac{f\left(x+su_1,y+su_2\right)-f\left(x,y\right)}{s} \\ &=\mathrm{\nabla f}\left(x,y\right)\cdot u \\ &= ||\nabla f || \cos\theta
\end{align*}
$$
The Gradient
$$
{\nabla\ f}\left(x,y,z\right)=\frac{\partial f}{\partial x}i+\frac{\partial f}{\partial y}j+\frac{\partial f}{\partial z}k
$$
Tangent line to a level curve of the form $f(x,y) = 0$ at a point $(x_0,y_0)$,
$$f_x(x_0,y_0)\left(x-x_0\right)+f_y(x_0,y_0)\left(y-y_0\right)=0$$
$$\frac{d}{dt}(f(r(t))=\nabla f(r(t))\cdot r'(t)$$
Tangent plane to $f\left(x,y,z\right) = c$ at the point $P(x_0,y_0,z_0)$,
$$f_x(P)\left(x-x_0\right)+f_y(P)\left(y-y_0\right)+f_z(P)\left(z-z_0\right)=0$$
Or when $f(x,y) =z$ at the point $P(x_0,y_0)$,
$$f_x(P)\left(x-x_0\right)+f_y(P)\left(y-y_0\right)-\left(z-z_0\right)=0$$
Normal line to $f\left(x,y,z\right) = c$ at the point $P(x_0,y_0,z_0)$,
$$
\begin{aligned}
x &= x_0+f_x(P)t \\
y &= y_0+f_y(P)t \\ 
z &= z_0+f_z(P)t
\end{aligned}
$$
Linear Approximation ($f(x,y) \approx L(x,y)$) of $f(x,y)$ at $(x_0,y_0)$,
$$L(x,y)=f(x_0,y_0)+f_x(x_0,y_0)(x-x_0)+f_y(x_0,y_0)(y-y_0)$$
Total Differential,
$$\begin{aligned}
df&=f_x\left(x_0,y_0\right)dx+f_y\left(x_0,y_0\right)dy \\
df&= (\nabla f(P_0) \cdot u) ds
\end{aligned}$$
Standard Linear Approximation Error where $M$ is the upper bound of the second partials on a rectangle centered at point $P$, 
$$\left|E\right|\le\frac{1}{2}M\left(\left|x-x_0\right|+\left|y-y_0\right|\right)^2$$
