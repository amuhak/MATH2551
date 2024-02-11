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
Derivative Along a Path,
$$\frac{d}{dt}(f(r(t))=\nabla f(r(t))\cdot r'(t)$$
