import React, { useState, useEffect } from 'react';
import { getCategories } from '../services/api';

const CategoryFilter = ({ onCategoryChange }) => {
  const [categories, setCategories] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchCategories = async () => {
      try {
        const data = await getCategories();
        setCategories(['All', ...data]);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchCategories();
  }, []);

  if (loading) return <div>Loading categories...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div className="mb-4">
      <label htmlFor="category-filter" className="mr-2 text-gray-300">Filter by category:</label>
      <select
        id="category-filter"
        onChange={(e) => onCategoryChange(e.target.value)}
        className="border border-gray-700 bg-gray-800 text-white p-2 rounded-md focus:outline-none focus:ring-2 focus:ring-violet-500"
      >
        {categories.map((category) => (
          <option key={category} value={category}>
            {category}
          </option>
        ))}
      </select>
    </div>
  );
};

export default CategoryFilter;
