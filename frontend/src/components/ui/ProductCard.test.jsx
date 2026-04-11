import { render, screen, fireEvent } from '@testing-library/react';
import { describe, it, expect, vi } from 'vitest';
import { ProductCard } from './ProductCard';

describe('ProductCard', () => {
  const mockProduct = {
    name: 'Test Product',
    price: '$99.99',
    imageUrl: 'test-image.jpg',
    onAddToCart: vi.fn(),
  };

  it('renders product information correctly', () => {
    render(<ProductCard {...mockProduct} />);

    expect(screen.getByText(mockProduct.name)).toBeInTheDocument();
    expect(screen.getByText(mockProduct.price)).toBeInTheDocument();

    const image = screen.getByRole('img');
    expect(image).toHaveAttribute('src', mockProduct.imageUrl);
    expect(image).toHaveAttribute('alt', mockProduct.name);
  });

  it('calls onAddToCart when the button is clicked', () => {
    render(<ProductCard {...mockProduct} />);

    const button = screen.getByRole('button', { name: /add to cart/i });
    fireEvent.click(button);

    expect(mockProduct.onAddToCart).toHaveBeenCalledTimes(1);
  });

  it('displays the correct button text', () => {
    render(<ProductCard {...mockProduct} />);
    expect(screen.getByText('Add to cart')).toBeInTheDocument();
  });
});
